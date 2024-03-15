const {
    createUserSignature,
    getKeyPairFromSignature,
} = require('@tanx-libs/tanx-connector');

const ethPrivateKey = process.argv[2]
let option = 'mainnet'

if (process.argv.length > 3){
    option = process.argv[3]
}

const userSignature = createUserSignature(ethPrivateKey, option) // or sign it yourself; default mainnet
const keyPair = getKeyPairFromSignature(userSignature.signature)

const stark_public_key = keyPair.getPublic().getX().toString('hex')
const stark_private_key = keyPair.getPrivate().toString('hex')

result = {
    stark_private_key: stark_private_key,
    stark_public_key: stark_public_key    
}

console.log(JSON.stringify(result));
