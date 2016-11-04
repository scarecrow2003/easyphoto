import AppDispatcher from '../../common/dispatchers/AppDispatcher';
import {ACTION_LIST_JOBS} from '../constants/JobConstants';
import JobServices from '../services/JobServices';

export default {
    getJobsList: () => {
        JobServices.getJobsList(function(response) {
            AppDispatcher.dispatch({
                actionType: ACTION_LIST_JOBS,
                jobs: response.jobs,
                companies: response.companies
            });
        })
    },

    saveJob: (data) => {
        JobServices.saveJob(data, function(response) {
            AppDispatcher.dispatch({
                actionType: ACTION_SAVE_JOB,
                data: response.data
            });
        })
    },

    updateJob: (data) => {
        JobServices.saveJob(data, function(response) {
            AppDispatcher.dispatch({
                actionType: ACTION_UPDATE_JOB,
                data: data
            });
        })
    }
}