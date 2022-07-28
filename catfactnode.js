'use strict';
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
module.exports.getItemDetails = async (event) => {
  let list = [
    "The longest living cat on record according to the Guinness Book belongs to the late Creme Puff of Austin, Texas who lived to the ripe old age of 38 years and 3 days!",
    "Cats have \"nine lives\" thanks to a flexible spine and powerful leg and back muscles",
    "A cat's nose pad is ridged with a unique pattern, just like the fingerprint of a human.",
    "Florence Nightingale owned more than 60 cats in her lifetime.",
    "A cat sees about 6 times better than a human at night, and needs 1/6 the amount of of light that a human does - it has a layer of extra reflecting cells which absorb light."
   ];
  let randomitem = getRandomInt(0, (list.length-1));
  let item = list[randomitem];
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Headers": "*", 
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": true,
      "Access-Control-Allow-Methods": "*",
    },
    body: JSON.stringify(
      {
        "fact": item,
        "length": item.length
      },
      null,
      2
    ),
  };

};