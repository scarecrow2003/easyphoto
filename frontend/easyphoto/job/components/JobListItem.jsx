import React from 'react';
import ListItem from '../../common/components/ListItem';
import JobActions from '../actions/JobActions';

export default class JobListItem extends ListItem {

    getTitle() {
        return this.props.item.customer_name;
    }

    deleteItem() {

    }

    editItem() {

    }

    getBody() {
        return (
            <form className="form-horizontal">
                <div className="form-group">
                    <label className="col-xs-6">Name:</label>
                    <div className="col-xs-6"><span>{this.props.item.customer_name}</span></div>
                </div>
            </form>
        );
    }
}