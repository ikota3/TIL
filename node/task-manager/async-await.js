// const doWork = async () => {
//   throw new Error("error!");
//   return "Tom";
// };

const add = (a, b) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (a < 0 || b < 0) {
        return reject("Numbers must be non-negative");
      }
      resolve(a + b);
    }, 2000);
  });
};
const doWork = async () => {
  const sum = await add(1, 2);
  const sum2 = await add(1, sum);
  const sum3 = await add(-3, sum2);
  return sum3;
};

doWork()
  .then((result) => {
    console.log(result);
  })
  .catch((e) => {
    console.log(e);
  });
