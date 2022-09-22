
import useSWR from 'swr'
export function useB() {
    const {data, error} = useSWR('dashboard', async() => {
        const response = await fetch('http://localhost:3000/emotion/5')
        const data = await response.json()
        return data
    })

    if (error) return 'An error has occured'
    if (!data) return 'Loading'

    return data
}