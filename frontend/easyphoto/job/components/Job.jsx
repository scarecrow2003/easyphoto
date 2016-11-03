import React from 'react';
import JobActions from '../actions/JobActions';
import JobStore from '../stores/JobStore';

export default class Job extends React.Component {

    constructor() {
        super();
        this.state = {
            jobs: []
        }
    }

    componentWillMount() {
        JobActions.getJobsList();
        this.changeListener = this._onChange.bind(this);
    }

    componentDidMount() {
        JobStore.addChangeListener(this.changeListener);
    }

    componentWillUnmount() {
        JobStore.removeChangeListener(this.changeListener);
    }

    _onChange() {
        this.setState({
            jobs: JobStore.jobs
        })
    }

    render() {
        return (
            <div>{this.state.jobs.length}</div>
        );
    }
}