#!/usr/bin/node

const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

try {
  const content1 = fs.readFileSync(sourceFile1, 'utf8');
  const content2 = fs.readFileSync(sourceFile2, 'utf8');
  const concatenatedContent = content1 + content2;
  fs.writeFileSync(destinationFile, concatenatedContent);
  console.log(`Concatenated files: ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
} catch (error) {
  console.error('Error:', error.message);
}
