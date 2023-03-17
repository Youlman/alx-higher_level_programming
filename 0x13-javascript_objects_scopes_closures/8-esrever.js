#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  for (let i = 0; i < list.length; i++) {
    array[i] = list[list.length - 1 - i];
  }
  return array;
};
