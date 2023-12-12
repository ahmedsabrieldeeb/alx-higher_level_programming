#!/usr/bin/node
const argv = process.argv.slice(2);

for (let i = 0; i < argv.length; i++) {
  argv[i] = Number(argv[i]);
}

if (argv.length <= 1) {
  console.log(0);
} else {
  const largeNumber = Math.max(...argv);
  argv.splice(argv.indexOf(largeNumber), 1);
  console.log(Math.max(...argv));
}
