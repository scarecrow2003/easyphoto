import React from 'react';
import localizer from 'react-widgets/lib/localizers/simple-number';
import {Nav, NavItem} from 'react-bootstrap';
import AddItem from '../../common/components/AddItem';
import JobListItem from './JobListItem';

export default class JobList extends React.Component {
    constructor() {
        super();
        this.state = this._getInitialState();
        localizer();
    }

    _getInitialState() {
        return {
            search: ''
        }
    }

    render() {
        var datas = [];
        if (this.state.search === '') {
            datas = this.props.datas.slice();
        } else {
            datas = this.props.datas.slice();
        }
        return (
            <div>
                <div className="col-xs-12">Search box</div>
                {datas.map(function(item, i) {
                    return (<JobListItem key={i} item={item} {...this.props} />);
                }, this)}
                <AddItem {...this.props}/>
            </div>
        );
    }
}