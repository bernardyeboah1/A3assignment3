let mongoose = require('mongoose');
// create a book model

let courseModel = mongoose.Schema({
  name: String,
  prof: String,
  start: String,
  end: String,
  grade: String

},
{
  collection: "courses" 
})
module.exports = mongoose.model('Course', courseModel);