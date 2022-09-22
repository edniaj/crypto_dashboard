import { useRouter } from "next/router"
import { useEffect, useState } from "react"
import Image from 'next/image'

export async function getServerSideProps() {
    const resp = await fetch(
        `https://jherr-pokemon.s3.us-west-1.amazonaws.com/pokemon/${id}.json`
    )
    return{
        props:{
            pokemon: await resp.json()
        }
    }
}

export default function Details() {

    const {
        query: { id }
    } = useRouter()
    const [pokemon, setPokemon] = useState(null)
    
    useEffect(() => {
        async function getPokemon() {
            
            setPokemon(await resp.json());
        }

        if (id) getPokemon()
    })

    
    return <>
        <div>
            Hello {id}
        </div>
        <div>
            <img 
                src={'https://jherr-pokemon.s3.us-west-1.amazonaws.com/images/ivysaur.jpg'}
                width={500}
                height={500}
            />
            {JSON.stringify(pokemon)}
        </div>

    </>
}