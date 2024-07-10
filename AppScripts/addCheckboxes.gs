function addCheckboxesEveryFourRowsFast() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName("DRAFT");
  var lastRow = sheet.getLastRow();
  
  // Create a checkbox criteria
  var criteria = SpreadsheetApp.newDataValidation().requireCheckbox().build();
  
  // Apply checkboxes to the entire column A
  sheet.getRange("A3:A" + lastRow).setDataValidation(null);
  
  // Apply checkboxes to every 4th row starting from row 3
  for (var i = 3; i <= lastRow; i += 4) {
    sheet.getRange(i, 1).setDataValidation(criteria);
  }
}