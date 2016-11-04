import React from 'react';
import {Button, Panel} from 'react-bootstrap';
import JobActions from '../actions/JobActions';
import JobStore from '../stores/JobStore';
import JobList from './JobList';
import JobEditItem from './JobEditItem';
import JobModel from '../models/JobModel';
import ModalComponent from '../../common/components/ModalComponent';

export default class Job extends React.Component {

    constructor() {
        super();
        this.state = {
            jobs: [],
            currentJob: {},
            showModal: false
        }
        this.add = this.add.bind(this);
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

    close() {
        this.setState({
            jobs: JobStore.jobs,
            showModal: false
        });
    }

    save() {
        if (this.refs["job-popup"].validateHasNoError()) {
            if (this.state.currentJob.id == null) {
                JobActions.saveJob(this.state.currentJob);
            } else {
                JobActions.updateJob(this.state.currentJob);
            }
            this.setState({showModal: false});
        }
    }

    add() {
        this.state.currentJob = new JobModel();
        this.setState({showModal: true});
    }

    render() {
        const actions = [<Button key="close" onClick={this.close.bind(this)}>Close</Button>, <Button key="save" className="btn-primary" onClick={this.save.bind(this)}>Save</Button>];
        return (
            <Panel>
                <div className="col-xs-12 page-main job-page">
                    <div className="col-xs-12 main-panel-header">
                        <div className="col-xs-12 page-title">
                            <h3>Jobs</h3>
                        </div>
                    </div>
                    <div className="col-xs-12 main-panel-content">
                        <JobList datas={this.state.jobs} add={this.add} />
                    </div>
                </div>
                <ModalComponent showModal={this.state.showModal} title={this.state.currentJob.id?"Edit Job":"Add Job"} actions={actions} close={this.close.bind(this)}>
                    <JobEditItem ref="job-popup" currentItem={this.state.currentJob} />
                </ModalComponent>
            </Panel>
        );
    }
}