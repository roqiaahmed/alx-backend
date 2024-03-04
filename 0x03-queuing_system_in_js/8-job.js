function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }
  for (let i = 0; i < jobs.length; i++) {
    const job = queue.create("push_notification_code_3", jobs[i]);
    job
      .on("enqueue", () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on("complete", () => {
        console.log("Notification job JOB_ID completed");
      })
      .on("failed attempt", (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      })
      .on("progress", (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
      .save();
  }
}

export default createPushNotificationsJobs;
