import type { AppProps } from 'next/app'
import 'antd/dist/antd.css';


function MyApp({ Component, pageProps }: AppProps & {Component : any} ) {

    /***
     * @ 14/9/2022
     * We are creating a SPA for now, might have to create multiple page in the future. Leave this code for now
     */

  if (Component.getLayout) return Component.getLayout(<Component {...pageProps}/>)

  return <Component {...pageProps} />
}

export default MyApp
