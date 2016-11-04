import Localization from 'react-localization';

export default {
    JOB_URL: '/private/rest/job/',
    ACTION_LIST_JOBS: 'LIST_JOBS',
    JOB_MESSAGES: new Localization({
        en: {
            list_job: "Jobs loaded",
            save_job: "Job saved",
            update_job: "Job updated"
        },
        cn: {
            list_job: "gongzuo jiazai wangbi",
            save_job: "Job saved",
            update_job: "Job updated"
        }
    })
}