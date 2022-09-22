import Footer from '../components/footer'
import Header from '../components/header'

export default function MyApp({Component, pageProps}) {

    if (Component.getLayout) return Component.getLayout(<Component {...pageProps}/>)

    return(

        <>
            <Component {...pageProps} />
        </>
    )
}