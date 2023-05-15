#!/usr/bin/node
function fac (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * fac(num - 1);
}

console.log(fac(parseInt(process.argv[2])));
