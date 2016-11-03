import AjaxUtil from '../../common/utils/AjaxUtil';
import {JOB_URL, JOB_MESSAGES} from '../constants/JobConstants';

class JobServices {
    getJobsList(success) {
        return AjaxUtil.ajaxGet(JOB_URL, success, null, null, false, JOB_MESSAGES.list_job);
    }
}

export default new JobServices();