import glob
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import matplotlib as mpl

def load_donor_languages():
	"""Load the donor languages from the saved TSV file"""
	try:
		donor_df = pd.read_csv('/Users/sina/GitHub/ConLoan/hidden/donors_CLAUDE.tsv', 
							  sep='\t', names=['language', 'word', 'donor'])
		return {(row['language'], row['word']): row['donor'] 
				for _, row in donor_df.iterrows()}
	except Exception as e:
		print(f"Error loading donor languages file: {str(e)}")
		return {}

def analyze_tsv_files(pattern='datasets/*_all_replacements.tsv'):
	results = {}
	donors_dict = load_donor_languages()
	files = glob.glob(pattern)
	
	for file_path in files:
		language = file_path.split('/')[-1].split('_')[0]
		
		try:
			df = pd.read_csv(file_path, sep='\t', header=None)
			
			if len(df.columns) >= 3:
				third_column_values = df[2].dropna().apply(lambda x: x.strip().lower()).tolist()
				
				for idx, row in df.iterrows():
					if pd.isna(row[2]):
						donor = donors_dict.get((language, row[0]))
						if donor:
							third_column_values.append(donor.strip().lower())
				
				value_counts = Counter(third_column_values)
				na_count = len(df) - len(third_column_values)
				if na_count > 0:
					value_counts['n/a'] = na_count
				
				results[language] = {
					'total_entries': len(df),
					'third_column_entries': len(third_column_values),
					'unique_values': len(value_counts) - (1 if 'n/a' in value_counts else 0),
					'value_counts': dict(value_counts)
				}
			else:
				results[language] = {
					'total_entries': len(df),
					'third_column_entries': 0,
					'unique_values': 0,
					'value_counts': {'n/a': len(df)}
				}
				
		except Exception as e:
			print(f"Error processing {file_path}: {str(e)}")
			
	return results

def aggregate_to_top_4(results):
	aggregated_results = {}
	for recipient, data in results.items():
		value_counts = data['value_counts']
		sorted_counts = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)
		top_4 = sorted_counts[:4]
		others_count = sum(count for _, count in sorted_counts[4:])
		aggregated_counts = {donor: count for donor, count in top_4}
		if others_count > 0:
			aggregated_counts['others'] = others_count
		aggregated_results[recipient] = aggregated_counts
	return aggregated_results

def create_visualization_with_custom_colors(results, output_file='donor_languages_plot.pdf'):
	mpl.rcParams['font.family'] = 'serif'
	aggregated_results = aggregate_to_top_4(results)
	
	# Prepare recipient languages first
	recipient_languages = list(aggregated_results.keys())
	recipient_languages = [lang.replace('-', ' ') for lang in recipient_languages]
	
	# Gather all donor languages and capitalize them
	donor_languages = sorted(
	    {donor.title() for data in aggregated_results.values() for donor in data.keys()},
	    key=lambda x: ('Z' if x.lower() == 'others' else x)  # This ensures "Others" goes last
	)
	
	# Define custom color palette with lowercase keys
	custom_colors = {
	    "others": "#2A363B",     # Deep charcoal
	    "arabic": "#FF847C",     # Soft coral
	    "english": "#99B898",    # Sage green
	    "french": "#E84A5F",     # Raspberry
	    "german": "#45B7D1",     # Ocean blue
	    "greek": "#4A90E2",      # Bright blue
	    "italian": "#6C5B7B",    # Dusty purple
	    "japanese": "#FFD700",   # Golden yellow
	    "latin": "#355C7D",      # Navy blue
	    "persian": "#C06C84",    # Mauve
	    "russian": "#A8E6CF",    # Mint green
	    "spanish": "#FF6B6B",    # Bright coral red
	    "turkish": "#DCEDC1"     # Light sage
	}
	
	# Create the color mapping for capitalized donor languages
	color_mapping = {donor: custom_colors.get(donor.lower(), plt.cm.tab20(i % 20)) 
					for i, donor in enumerate(donor_languages)}
	
	# Prepare data matrix
	data_matrix = np.zeros((len(recipient_languages), len(donor_languages)))
	
	# Fill the data matrix using lowercase comparison
	for i, recipient in enumerate(recipient_languages):
		orig_recipient = list(aggregated_results.keys())[i]  # Get original recipient name
		for j, donor in enumerate(donor_languages):
			donor_lower = donor.lower()
			data_matrix[i, j] = aggregated_results[orig_recipient].get(donor_lower, 0)
	
	# Create the visualization
	plt.figure(figsize=(14, 8))
	
	# Create the stacked bar chart
	bottom = np.zeros(len(recipient_languages))
	
	for i, donor in enumerate(donor_languages):
		plt.bar(
			recipient_languages,
			data_matrix[:, i],
			bottom=bottom,
			label=donor,
			color=color_mapping[donor]
		)
		bottom += data_matrix[:, i]
	
	plt.ylabel('Number of Words', fontsize=14)
	plt.xticks(rotation=45, fontsize=14, ha='right')
	plt.yticks(fontsize=14)
	
	# Set y-axis limit
	plt.ylim(0, 3200)
	
	# Adjust legend
	plt.legend(title='Donor Languages', fontsize=12, title_fontsize=12,
			  bbox_to_anchor=(1, 1), loc='upper right', ncol=1,
			  frameon=True, edgecolor='black', facecolor='white', framealpha=1)
	
	# Add totals above each bar
	for i, total in enumerate(bottom):
		plt.text(i, total + 50, str(int(total)), ha='center', va='bottom',
				fontsize=10, fontweight='bold', color='black')
	
	# Light gridlines
	plt.grid(axis='y', linestyle='--', alpha=0.7)
	
	plt.tight_layout()
	
	# Save the plot
	plt.savefig(output_file, format='pdf', bbox_inches='tight')
	print(f"Plot saved as {output_file}")
	
	return plt.gcf()

# Run the analysis
results = analyze_tsv_files()

# Create and show the visualization
fig = create_visualization_with_custom_colors(results)
plt.show()

# Print results
for language, data in results.items():
	print(f"\nAnalysis for {language}:")
	print(f"Total entries: {data['total_entries']}")
	print(f"Entries with third column: {data['third_column_entries']}")
	print(f"Unique values in third column: {data['unique_values']}")
	
	if data['value_counts']:
		print("\nValue counts:")
		sorted_items = sorted(data['value_counts'].items(),
							key=lambda x: ('Z' if x[0] == 'n/a' else x[0]))
		for value, count in sorted_items:
			print(f"  {value}\t {count}")