import type { NextPage } from 'next'
import Head from 'next/head'
import styles from '../styles/Home.module.css'


const Home: NextPage = () => {
  
return(
    <>
      <div className={styles.container}>
        <Head>
          <title>Dashboard</title>
          <link rel="icon" href="/crypto.png" />
        </Head>
      </div>
      <div>
        hi
      </div>
    </>)
  
}

// export async function getServerSideProps(req: NextApiRequest, res: NextApiResponse) {

//   /***
//    * 
//    * @ 14/9/2022 JD
//    * Remember to re-seed the data 
//    * 
//    * @ 14/9/2022 JD
//    * Caching, I think dashboard don't require this shit. We can use this on something else
//    *  */
//   // res.setHeader(
//   //   'Cache-Control',
//   //   'public, s-maxage=10, stale-while-revalidate=59'
//   // )

//   return {
//     props: {},
//   }
// }


export default Home