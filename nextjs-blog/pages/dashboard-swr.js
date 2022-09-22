import useSWR from "swr";
import { useB } from "../hooks";

function DashboardSWR() {
    // since its a hook, we call it inside the component
    // arg1 unique key, arg2 fetcher

    const {data,error} = useB()



    return (<div>
        <h2>Dashboard</h2>
        <h2>POST - {JSON.stringify(data)}</h2>
    </div>)
}

export default DashboardSWR