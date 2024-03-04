import kue from "kue";

import createPushNotificationsJobs from "./8-job.js";
const queue = kue.createQueue();
