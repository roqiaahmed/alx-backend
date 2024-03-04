const redis = require("redis");
const { promisify } = require("util");

const client = redis.createClient();
client.on("connect", () => console.log("Redis client connected to the server"));

client.on("error", (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  await client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
