function highlightText() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("DRAFT");
  var range = sheet.getRange("A:A"); // Select only column A
  var values = range.getValues();

  // Function to get the words around the tags
  function getSurroundingWords(text, startPos, endPos, wordCount = 2) {
    const words = text.split(/(\s+)/); // Split by whitespace, keeping the separators
    let startWordIndex = 0;
    let endWordIndex = words.length - 1;

    // Calculate the start position for preceding words
    for (let i = 0, currentPos = 0; i < words.length; i++) {
      currentPos += words[i].length;
      if (currentPos >= startPos) {
        startWordIndex = Math.max(0, i - wordCount * 2); // Each word has a separator
        break;
      }
    }

    // Calculate the end position for following words
    for (let i = words.length - 1, currentPos = text.length; i >= 0; i--) {
      currentPos -= words[i].length;
      if (currentPos <= endPos) {
        endWordIndex = Math.min(words.length - 1, i + wordCount * 2);
        break;
      }
    }

    // Calculate the actual positions
    let precedingStart = 0;
    for (let i = 0; i < startWordIndex; i++) {
      precedingStart += words[i].length;
    }

    let followingEnd = 0;
    for (let i = 0; i <= endWordIndex; i++) {
      followingEnd += words[i].length;
    }

    return { precedingStart, followingEnd, wordCountBefore: startWordIndex / 2, wordCountAfter: (words.length - 1 - endWordIndex) / 2 };
  }

  // Loop through each cell in column A
  for (var i = 0; i < values.length; i++) {
    var cell = sheet.getRange(i + 1, 1); // Only column A
    var cellValue = values[i][0];
    var richTextBuilder = SpreadsheetApp.newRichTextValue().setText(cellValue);

    // Find the text between <L1>...</L1> and <N1></N1>
    var matches = [...cellValue.matchAll(/<(L\d+)>(.*?)<\/\1>|<(N\d+)><\/\3>/g)];
    matches.forEach(match => {
      let startTag, endTag, startPos, endPos;

      if (match[2]) {
        startTag = `<${match[1]}>`;
        endTag = `</${match[1]}>`;
        startPos = match.index;
        endPos = startPos + match[0].length;

        // Apply text style to the entire match (including tags)
        richTextBuilder.setTextStyle(startPos, endPos, SpreadsheetApp.newTextStyle()
          .setForegroundColor("#FF0000") // Red text color
          .setBold(true) // Bold text
          .build());
      } else {
        startTag = `<${match[3]}>`;
        endTag = `</${match[3]}>`;
        startPos = match.index;
        endPos = startPos + match[0].length;

        // Apply text style to the entire match (including tags)
        richTextBuilder.setTextStyle(startPos, endPos, SpreadsheetApp.newTextStyle()
          .setForegroundColor("#00008B") // Dark blue text color
          .setBold(true) // Bold text
          .build());
      }

      // Apply italic and dark green color to the surrounding words
      const { precedingStart, followingEnd, wordCountBefore, wordCountAfter } = getSurroundingWords(cellValue, startPos, endPos);
      if (wordCountBefore >= 2) {
        richTextBuilder.setTextStyle(precedingStart, startPos, SpreadsheetApp.newTextStyle()
          .setForegroundColor("#666666") 
          .setItalic(true) // Italic text
          .build());
      }
      if (wordCountAfter >= 2) {
        richTextBuilder.setTextStyle(endPos, followingEnd, SpreadsheetApp.newTextStyle()
          .setForegroundColor("#666666") 
          .setItalic(true) // Italic text
          .build());
      }
    });

    // Update the cell with the new rich text value
    cell.setRichTextValue(richTextBuilder.build());
  }
}
