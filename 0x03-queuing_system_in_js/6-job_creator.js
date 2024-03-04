const kue = require("kue");

const queue = kue.createQueue();

const data_job = {
  phoneNumber: "4153518780",
  message: "This is the code to verify your account",
};

var job = queue.create("push_notification_code", data_job).save();
job
  .on("enqueue", () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on("complete", () => {
    console.log("Notification job completed");
  })
  .on("failed attempt", () => {
    console.log("Notification job failed");
  });
