import { ITwitterInfoAll, IStalkingLogsheet, ITwitterUser } from './type/index';
import { UseTwitterDb, UseViewport } from './hooks'


import { Space, Table, Tag } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import { TwitterOutlined, GlobalOutlined } from '@ant-design/icons';

import React, { useEffect, useState } from 'react';



function DashboardSwr() {

    /***
     * 
     * @ 17/9/2022 JD
     *  Add a proper sorting function, sorting funtion isn't working
     * 
     * @ 16/9/2022 JD
     * Maybe we can include everyth in modal when user clicks on profile
     * will also do reverse lookup for new_following profile
     * 
     * Maybe we can add filters into the hook i.e. pagination
     * 
     * I think return recent 1000 logsheet should be enough. (can do some pagination on django model if we really need to lol - overkill)
     * for twitter_users, i think we can use prefetch to return only relevant users
     */

    const { isViewportXS } = UseViewport();

    const handleSortCreation = (x: IStalkingLogsheet,y: IStalkingLogsheet) => {
        
        let x_twitter_id = x.new_following_twitter_id 
        let x_date_added = data.twitter_users[x_twitter_id]?.created_at
        
        let y_twitter_id = y.new_following_twitter_id 
        let y_date_added = data.twitter_users[y_twitter_id]?.created_at

        return new Date(x_date_added).getTime() - new Date(y_date_added).getTime()
    }


    const handleSortDateAdded = (x: IStalkingLogsheet,y: IStalkingLogsheet) => {
        
        let x_twitter_id = x.new_following_twitter_id 
        let x_date_added = data.twitter_users[x_twitter_id]?.date_added
        
        let y_twitter_id = y.new_following_twitter_id 
        let y_date_added = data.twitter_users[y_twitter_id]?.date_added

        return new Date(x_date_added).getTime() - new Date(y_date_added).getTime()
    }

    const columns = [
        {
            title: 'Stalker alias',
            dataIndex: 'stalking_twitter_id',
            key: 'name',
            render: (text: string) => <h4>
                {data?.twitter_users[text]?.name_alias}
                <br />
                <a style={{ fontSize: '1.5em' }}
                    href={`https://www.twitter.com/${data?.twitter_users[text]?.username}`} target='blank'
                >
                    <TwitterOutlined
                    />
                </a>
                <a style={{ fontSize: '1.5em', marginLeft: '0.5em' }} href={data?.twitter_users[text]?.url} target='blank'>
                    {data?.twitter_users[text]?.url ? <GlobalOutlined /> : ''}
                </a>
            </h4>,
            // fixed: 'left',
            width: isViewportXS() ? 100 : 150
        },
        {
            title: 'New Following alias',
            dataIndex: 'new_following_twitter_id',
            key: 'age',
            render: (text: string) => <h4>
                {data?.twitter_users[text]?.name_alias}
                <br />
                <a
                    style={{ fontSize: '1.5em' }}
                    href={`https://www.twitter.com/${data?.twitter_users[text]?.username}`} target='blank'
                >
                    <TwitterOutlined
                    />
                </a>
                <a style={{ fontSize: '1.5em', marginLeft: '0.5em' }} href={data?.twitter_users[text]?.url} target='blank'>
                    {data?.twitter_users[text]?.url ? <GlobalOutlined /> : ''}
                </a>
            </h4>,
            width: isViewportXS() ? 100 : 250
            // fixed: 'left'
        },
        {
            title: 'Description',
            dataIndex: 'new_following_twitter_id',
            key: 'description',
            render: (text: string) => <div style={{ minWidth: '200px' }}>
                <h4>
                    {data?.twitter_users[text]?.description}
                </h4>
            </div>,
            width: isViewportXS() ? 220 : 600
        },
        {
            title: 'Account creation',
            dataIndex: 'new_following_twitter_id',
            key: 'created_at',
            render: (text: string) => {
                let date_ = data?.twitter_users[text]?.created_at
                if (date_) {
                    return <h4>{new Date(date_).toISOString().substring(0, 10)}</h4>
                }
            },
            fixed: isViewportXS() ? false : 'right',
            width: 106,
            sorter: (x:IStalkingLogsheet,y: IStalkingLogsheet) => handleSortCreation(x,y)
        },
        {
            title: 'Date added',
            dataIndex: 'date_added',
            key: 'address',
            render: (date_: Date) => {
                const date = new Date(date_)
                return (
                    <h4>
                        {date.toISOString().substring(0, 10)}
                    </h4>)
            },
            fixed: 'right',
            width: isViewportXS() ? 60 : 106,
            sorter: (x:IStalkingLogsheet,y: IStalkingLogsheet) =>handleSortDateAdded(x,y)
        },
    ];


    const { data, error, mutate }: { data?: ITwitterInfoAll, error?: any, mutate?: any }  = UseTwitterDb()



    return (
        <>
            <Table
                columns={columns}
                dataSource={data?.stalking_logsheet}
                style={{ margin: "5vw", marginBottom: '10vh' }}
            // scroll={{ x: 800 }}
            />
        </>
    )
}

export default DashboardSwr