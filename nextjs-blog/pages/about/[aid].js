import { useRouter } from "next/router";


const baseUrl = `https://jsonplaceholder.typicode.com/albums/`

/**
 * Statis generation
 * getStaticPaths
 * getStaticProps
 * 
 * Server-side Rendering
 * getServerSideProps
 
 */


// export async function getStaticPaths(aid) {
// // this is to throw into getStaticProps which path you are suppose to render
// // This also tells nextjs which page to render and which page to return 404
//     const res = await fetch(baseUrl)
//     const albums = await res.json()

//     const paths = albums.map(album => ({
//         params: {aid: JSON.stringify(album?.id)}
//     }))

//     return {paths, fallback:false}

// }

export async function getServerSideProps({params}){
    
    const res = await fetch(`${baseUrl}${params?.aid}`)
    const post = await res.json()

    return {props: {post}}
}

function Post({post}){
    return <>
        <div>
            {JSON.stringify(post)}
        </div>
    </>
}
export default Post