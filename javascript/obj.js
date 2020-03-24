function removeProperty(obj, prop) {
    console.log(obj)
    if (typeof obj.prop === undefined) {
        return false;
    }
    delete obj.prop;
    console.log(obj);
    return true;
}

const person = {
    name: ('Fatma')
}

console.log(removeProperty(person, 'name'))
    // console.log(person)