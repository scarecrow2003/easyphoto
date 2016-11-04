import BaseStore from '../../common/stores/BaseStore';

class JobStore extends BaseStore {
    constructor() {
        super();
        this.subscribe(() => this._registerToActions.bind(this));
        this._jobs = [];
        this._companies = [];
    }

    get jobs() {
        return this._jobs;
    }

    _registerToActions(action) {
        switch (action.actionType) {
            case ACTION_LIST_JOBS:
                this._jobs = action.jobs;
                this._companies = action.companies
                this.emitChange();
                break;
            default:
                break;
        }
    }
}

export default new JobStore();