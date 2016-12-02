import {ACTION_ADD_JOB} from '../constants/JobConstants';

const jobReducer = (state, action) => {
    switch (action.type) {
        case ACTION_ADD_JOB:
            return Object.assign({}, state, {
                jobs: [
                    ...state.jobs,
                    action.data
                ]
            });
        default:
            return state;
    }
};

export default jobReducer;