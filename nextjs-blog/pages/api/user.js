export default function (req, res) {
    console.log(req)
    
    // res.status(200).json({name:'john'})
    switch (req.method) {
        case 'POST':
            res.status(200).json({ name: 'John Doe', method: 'POST' })
        case 'GET':
            res.status(200).json({ name: 'John Doe', method: 'GET' })
        case 'PATCH':
            res.status(200).json({method:'PATCH'})
    }
}