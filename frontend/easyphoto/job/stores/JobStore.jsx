import BaseStore from '../../common/stores/BaseStore';

class JobStore extends BaseStore {
    constructor() {
        super();
        this.subscribe(() => this._registerToActions.bind(this));
        this._jobs = [];
    }

    get jobs() {
        return this._jobs;
    }

    _registerToActions(action) {
        switch (action.actionType) {
            case ACTION_LIST_JOBS:
                this._jobs = action.data;
                this.emitChange();
                break;
            default:
                break;
        }
    }
}

export default new JobStore();