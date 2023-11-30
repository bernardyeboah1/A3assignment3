var express = require('express');
var router = express.Router();
//const { router } = require('../config/app');
let Course = require('../models/Bio_courses');

module.exports.DislayCourselist = async (req,res,next)=>{ //< Mark function as async
    try{
       const CourseList = await Course.find(); //< Use of await keyword
       res.render('course/list', {
          title: 'Course List', 
          CourseList: CourseList
       });
    }catch(err){
       console.error(err);
       //Handle error
       res.render('course/list', {
          error: 'Error on server'
       });
    }
 };

 module.exports.AddCourse = async (req,res,next)=>{
    try{
        res.render('course/add',
        {
            title:'Add Course'
        })
    }
    catch(err)
    {
        console.error(err);
        res.render('course/list',
        {
            error: 'Error on the server'
        });
    }
};

module.exports.ProcessCourse = async (req,res,next)=>{
    try{
        let newCourse = Course({
            "name":req.body.name,
            "prof": req.body.prof,
            "start": req.body.start,
            "end": req.body.end,
            "grade": req.body.grade
        });
        Course.create(newCourse).then(() =>{
            res.redirect('/courselist')
        })
    }
    catch(error){
        console.error(err);
        res.render('course/list',
        {
            error: 'Error on the server'
        });
    }
};

module.exports.EditCourse = async (req,res,next)=>{
    try{
    const id = req.params.id;
    const CourseToEdit = await Course.findById(id);
    res.render('course/edit',
    {
        title:'Edit Course',
        Course:CourseToEdit
    })
}
catch(error){
    console.error(err);
    res.render('course/list',
    {
        error: 'Error on the server'
    });
}
}

module.exports.ProcessEditCourse = (req,res,next)=>{
    try{
        const id = req.params.id;
        let updatedCourse = Course({
            "_id":id,
            "name":req.body.name,
            "prof": req.body.prof,
            "start": req.body.start,
            "end": req.body.end,
            "grade": req.body.grade
        });
        Course.findByIdAndUpdate(id,updatedCourse).then(()=>{
            res.redirect('/courselist')
        });
    }
    catch(error){
        console.error(err);
        res.render('course/list',
        {
            error: 'Error on the server'
        });
    }
};

module.exports.DeleteCourse = (req,res,next)=>{
    try{
        let id = req.params.id;
        Course.deleteOne({_id:id}).then(() =>
        {
            res.redirect('/courselist')
        })
    }
    catch(error){
        console.error(err);
        res.render('course/list',
        {
            error: 'Error on the server'
        });
    }
}