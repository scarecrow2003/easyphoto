import BaseModel from 'common/models/BaseModel';

export default class JobModel extends BaseModel {

    constructor() {
        super();
        this.id  = null;
        this.customer_name = 'Test';
    }

}
