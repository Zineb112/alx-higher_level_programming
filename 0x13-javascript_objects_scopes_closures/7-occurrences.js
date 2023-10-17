#!/usr/bin/node

exports.nbOccurences = function (list, searchElement)
{
	// Use the filter function to count occurrences of the search element
	const occurrences = list.filter(item => item === searchElement);
	return occurrences.length;
};
