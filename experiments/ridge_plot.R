# Libraries
library(ggplot2)
library(ggridges)
library(dplyr)
library(tidyr)

# Directory containing your files
files_dir <- "LoanwordAnnotation/frequencies/"

# List of files
files <- c(
  "Northern-Kurdish_frequencies.tsv", "Chinese_frequencies.tsv", "French_frequencies.tsv",
  "German_frequencies.tsv", "Greek_frequencies.tsv", "Icelandic_frequencies.tsv",
  "Italian_frequencies.tsv", "Portuguese_frequencies.tsv", "Russian_frequencies.tsv",
  "Spanish_frequencies.tsv"
)

# Load and combine all files into one data frame
all_data <- do.call(rbind, lapply(files, function(file) {
  file_path <- paste0(files_dir, file)
  df <- read.delim(file_path, header=FALSE, stringsAsFactors=FALSE)
  names(df) <- c("word1", "word2", "loan_freq", "native_freq")
  
  # Add a language column
  df$language <- sub("_frequencies.tsv", "", file)
  
  # Convert frequencies to numeric
  df$loan_freq <- as.numeric(df$loan_freq)
  df$native_freq <- as.numeric(df$native_freq)
  
  # Filter out rows with missing values
  df <- df %>%
    filter(!is.na(loan_freq), !is.na(native_freq))
  
  # Replace zeros with a very small positive number (to avoid log10 issues)
  df$loan_freq[df$loan_freq == 0] <- 1e-10
  df$native_freq[df$native_freq == 0] <- 1e-10
  
  # Convert to long format
  df_long <- data.frame(
    frequency = c(df$loan_freq, df$native_freq),
    type = rep(c("Loanword", "Native"), each=nrow(df)),
    language = df$language
  )
  return(df_long)
}))

all_data <- all_data %>%
  distinct(language, type, frequency)

# Plot with increased font size, serif font, no legend title, and serif font in the legend
ggplot(all_data, aes(x = frequency, y = language, fill = type)) +
  geom_density_ridges(alpha = 0.6, scale = 1) +
  scale_x_log10() +
  coord_cartesian(xlim = c(1e-9, 1e-2)) +  # Adjust x-axis limits
  labs(
    x = "Corpus-based Normalized Frequency (log scale)",
    y = "Language"
  ) +
  theme_minimal(base_size = 14) +  # Set font size to 11pt
  scale_fill_manual(values = c("Loanword" = "#377eb8", "Native" = "#e41a1c")) +
  scale_y_discrete(labels = function(x) gsub("Northern-Kurdish", "Kurdish", x)) +  # Custom y-axis label
  theme(
    legend.position = "top",
    legend.text = element_text(family = "serif", size = 14),  # Set legend text to serif
    legend.title = element_text(family = "serif", size = 14),  # Set legend title to serif (even though title is removed)
    axis.text.y = element_text(size = 14, family = "serif"),  # Increase axis font size and set to serif
    axis.text.x = element_text(size = 14, family = "serif"),  # Set x-axis text to serif
    axis.title.x = element_text(size = 14, family = "serif"),  # Set x-axis title to serif
    axis.title.y = element_text(size = 14, family = "serif"),  # Set y-axis title to serif
    plot.title = element_text(size = 14, family = "serif")  # Set plot title to serif with larger font
  ) +
  guides(fill = guide_legend(title = NULL))  # Remove the legend title (but keep the legend itself)


# Calculate mean frequencies for Loanword and Native per language
mean_freq <- all_data %>%
  group_by(language, type) %>%
  summarize(mean_frequency = mean(frequency, na.rm = TRUE)) %>%
  pivot_wider(names_from = type, values_from = mean_frequency)

# Display the result
print(mean_freq)


