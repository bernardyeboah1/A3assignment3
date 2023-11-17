let express = require('express');
let router = express.Router();
let mongoose = require('mongoose');

//connect with course model

let Course = require('../models/courses');
const e = require('express');

// Read Operation
// Get route for course list

router.get('/', (req,res,next)=>{
  Course.find((err,CourseList)=>{
    if(err)
    {
      return console.error(err)
    }
    else
    {
      res.render('course/list'
      ,{title:'Courses', 
      CourseList:courselist})
    }

  });
});

// Add operation
// Get route for displaying the Add-Page --Create Operation
router.get('/add', (req,res,next)=> {
  res.render('course/add', {title:'Add Course'})
});
// Post route for processing the Add-Page --Create Operation
router.post('/add', (req,res,next)=> {
  let newCourse = Course ({
    "name" : req.body.name,
    "prof" : req.body.prof,
    "start" : req.body.start,
    "end" : req.body.end,
    "grade" : req.body.grade
  });
  Course.create(newCourse, (err,Course) => {
    if(err)
    {
      console.log(err);
      res.end(err);
    }
    else
    {
      res.redirect('/course/list');
    }
  })

});

// Edit Operation
router.get('/edit/:id', (req,res,next)=> {
  let id = req.params.id;
  Course.findById(id,(err,courseToEdit)=>{
    if(err)
    {
      console.log(err);
      res.end(err);
    }
    else
    {
      res.render('course/edit',{title: 'Edit Course', course:courseToEdit});
    }

  });


});
// Get route for displaying the Edit Operation -- Update Operation 
// Post route for displaying the Update Operation -- Create Operation
router.post('/edit/:id', (req,res,next)=> {
  let id=req.params.id;
  let updateCourse = Course({
    "_id":id,
    "name" : req.body.name,
    "prof" : req.body.prof,
    "start" : req.body.start,
    "end" : req.body.end,
    "grade" : req.body.grade

  });
  Course.updateOne({_id :id},updateCourse, (err) =>{
    if(err)
    {
      console.log(err);
      res.end(err);
    }
    else
    {
      res.redirect('/course/list');
    }

  });



});

// Delete Operation
// Get to perform the Delete Operation -- Deletion

router.get('/delete/:id', (req,res,next)=> {
  let id = req.params.id;
  Course.deleteOne({_id:id},(err)=>{
    if(err)
    {
      console.log(err);
      res.end(err);
    }
    else
    {
      res.redirect('/course-list');
    }
  });

});




module.exports=router;
