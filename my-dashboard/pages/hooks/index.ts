import { ITwitterInfoAll } from './../type/index';
import useSWR from 'swr'
import React, { useState, useEffect } from 'react';

const { NEXT_PUBLIC_DATABASE_URL } = process.env
const fetchConfig: any = new Headers({
    'Access-Control-Allow-Origin': '*',
    mode: 'cors'
})


/***
 * @ 16/9/2022
 * We are only using  useSWR for simple polling, not messing around with the cache atm
 * Maybe we can use this for something else when we are scalinge huge
 * useSwr is a hook, it has it's own state. Just pull data and use the data inside the component similar to the state. Mutate if you need to config local data fast
 * 
*/


export function UseViewport() {
    const [viewportWidth, setViewportWidth] = useState(0)
    useEffect(() => {
        const interval = setInterval(() => {
            setViewportWidth(window.innerWidth)
        }, 100)
        return () => clearInterval(interval)
    }, [])

    function isViewportXS() {
        return viewportWidth < 576
    }
    function isViewportSM() {
        return viewportWidth <768
    }
    function isViewportMD() {
        return viewportWidth < 992
    }
    return {
        isViewportXS,
        isViewportSM,
        isViewportMD,
    }
}

export function UseTwitterDb() {

    fetchConfig.append('method', 'GET')

    const fetcher = (url: string) => fetch(url, fetchConfig)
        .then(res => res.json())

    const endpoint = `${NEXT_PUBLIC_DATABASE_URL}twitter/all_twitter_info`
    const { data, error, mutate }: { data?: ITwitterInfoAll, error?: any, mutate?: any } = useSWR(endpoint, fetcher, { refreshInterval: 5000 })

    return {
        data,
        error,
        mutate
    }
}

// Placeholder for testing website
// export default function UsePlaceholder() {
//     const fetcher = url => fetch(url, fetchConfig)
//         .then(res => res.json())
//     const { data } = useSWR('/api/user/', fetcher, { refreshInterval: 1000 })

//     return { data }
// }