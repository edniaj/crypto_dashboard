import type { NextApiRequest, NextApiResponse } from 'next'
import { useRouter } from 'next/router'

export default function handler(req:NextApiRequest,res:NextApiResponse) {
    const id = req.query.id
    res.status(200).json({name:id})
}