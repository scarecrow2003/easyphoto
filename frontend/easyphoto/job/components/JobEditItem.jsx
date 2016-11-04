import React from 'react';
import ValidatedForm from '../../form/components/ValidatedFormHorizontal';

export default class JobEditItem extends React.Component {
    constructor(props) {
        super();
        this.state = ({
            job: props.currentItem
        });
        this.noError = true;
    }

    requestChange(type, value) {

    }

    getChildErrors(errorMsg){
        this.noError = false;
    }

    validateHasNoError() {
        this.noError = true;
        /*if (!this.isStop) {
            this.refs["amount"].activateValidation();
        }
        if (this.state.expense.expense_type === null || this.state.expense.expense_type === "OTHERS") {
            this.refs["description"].activateValidation();
        }*/
        return this.noError;
    }

    render() {
        return (
            <ValidatedForm className="form-horizontal form-horizontal-edit">
                <div className="form-group">
                    <label className="col-xs-4">Name:</label>
                    <div className="col-xs-8">

                    </div>
                </div>
            </ValidatedForm>
        );
    }
}