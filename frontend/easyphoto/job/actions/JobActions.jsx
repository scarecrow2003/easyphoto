import AppDispatcher from '../../common/dispatchers/AppDispatcher';
import {ACTION_LIST_JOBS} from '../constants/JobConstants';
import JobServices from '../services/JobServices';

export default {
    getJobsList: () => {
        JobServices.getJobsList(function(response) {
            AppDispatcher.dispatch({
                actionType: ACTION_LIST_JOBS,
                data: response.data
            });
        })
    }
}