import useSWR from 'swr'



function Profile() {

    const fetcher = (...args) => fetch(...args).then(res => res.json())


    const { data, error } = useSWR('/api/emotion/123', fetcher)

    if (error) return <div>failed to load</div>
    if (!data) return <div>loading...</div>

    // render data
    return <div>hello {data.name}!</div>
}

export default Profile