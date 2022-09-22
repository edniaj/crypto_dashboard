import { useRouter } from "next/router"
import Footer from "../../components/footer"
import Header from "../../components/header"
import Layout from "../../components/layout"



const baseUrl = `https://jsonplaceholder.typicode.com/albums/`

export async function getStaticProps() {

    const res = await fetch(baseUrl)
    const albums = await res.json()

    return {
        props: {
            albums
        }
    }
}

export default function About({ albums }) {

    const router = useRouter()

    return (<>

        <ul>
            {albums?.map(album => {
                return <div style={{ border: '1px solid black' }} onClick={() => {
                    router.push({
                        pathname: '/about/[aid]',
                        query: { aid: album?.id }
                    })
                }}>
                    <ol>
                        <li>{album?.userId}</li>
                        <li>{album?.title}</li>
                    </ol >
                </div>
            }).slice(0, 3)}
        </ul>
    </>)
}

About.getLayout = function PageLayout(page) {
    return (
        <>
            <Header />
            {page}
            <Footer />
        </>
    )
}