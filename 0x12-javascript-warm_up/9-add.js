#!/usr/bin/node
const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(firstArg, secondArg));
