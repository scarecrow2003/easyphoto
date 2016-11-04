import AjaxUtil from '../../common/utils/AjaxUtil';
import {JOB_URL, JOB_MESSAGES} from '../constants/JobConstants';

class JobServices {
    getJobsList(success) {
        return AjaxUtil.ajaxGet(JOB_URL, success, null, null, false, JOB_MESSAGES.list_job);
    }

    saveJob(data, success) {
        return AjaxUtil.ajaxPost(JOB_URL, data, success, null, null, false, data.id?JOB_MESSAGES.update_job:JOB_MESSAGES.save_job);
    }
}

export default new JobServices();