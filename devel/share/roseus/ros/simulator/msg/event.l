;; Auto-generated. Do not edit!


(when (boundp 'simulator::event)
  (if (not (find-package "SIMULATOR"))
    (make-package "SIMULATOR"))
  (shadow 'event (find-package "SIMULATOR")))
(unless (find-package "SIMULATOR::EVENT")
  (make-package "SIMULATOR::EVENT"))

(in-package "ROS")
;;//! \htmlinclude event.msg.html


(defclass simulator::event
  :super ros::object
  :slots (_generator_id _ID _type _generation_date _gen_time _completed_date _compl_time _route _split_attribute1 _split1 _split_attribute2 _split2 _split_attribute3 _split3 _attribute2 _value2 _attribute3 _value3 _last_event _first_event ))

(defmethod simulator::event
  (:init
   (&key
    ((:generator_id __generator_id) "")
    ((:ID __ID) 0)
    ((:type __type) "")
    ((:generation_date __generation_date) (instance ros::time :init))
    ((:gen_time __gen_time) "")
    ((:completed_date __completed_date) (instance ros::time :init))
    ((:compl_time __compl_time) "")
    ((:route __route) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:split_attribute1 __split_attribute1) "")
    ((:split1 __split1) 0.0)
    ((:split_attribute2 __split_attribute2) "")
    ((:split2 __split2) 0.0)
    ((:split_attribute3 __split_attribute3) "")
    ((:split3 __split3) 0.0)
    ((:attribute2 __attribute2) "")
    ((:value2 __value2) 0.0)
    ((:attribute3 __attribute3) "")
    ((:value3 __value3) 0.0)
    ((:last_event __last_event) nil)
    ((:first_event __first_event) nil)
    )
   (send-super :init)
   (setq _generator_id (string __generator_id))
   (setq _ID (round __ID))
   (setq _type (string __type))
   (setq _generation_date __generation_date)
   (setq _gen_time (string __gen_time))
   (setq _completed_date __completed_date)
   (setq _compl_time (string __compl_time))
   (setq _route __route)
   (setq _split_attribute1 (string __split_attribute1))
   (setq _split1 (float __split1))
   (setq _split_attribute2 (string __split_attribute2))
   (setq _split2 (float __split2))
   (setq _split_attribute3 (string __split_attribute3))
   (setq _split3 (float __split3))
   (setq _attribute2 (string __attribute2))
   (setq _value2 (float __value2))
   (setq _attribute3 (string __attribute3))
   (setq _value3 (float __value3))
   (setq _last_event __last_event)
   (setq _first_event __first_event)
   self)
  (:generator_id
   (&optional __generator_id)
   (if __generator_id (setq _generator_id __generator_id)) _generator_id)
  (:ID
   (&optional __ID)
   (if __ID (setq _ID __ID)) _ID)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:generation_date
   (&optional __generation_date)
   (if __generation_date (setq _generation_date __generation_date)) _generation_date)
  (:gen_time
   (&optional __gen_time)
   (if __gen_time (setq _gen_time __gen_time)) _gen_time)
  (:completed_date
   (&optional __completed_date)
   (if __completed_date (setq _completed_date __completed_date)) _completed_date)
  (:compl_time
   (&optional __compl_time)
   (if __compl_time (setq _compl_time __compl_time)) _compl_time)
  (:route
   (&optional __route)
   (if __route (setq _route __route)) _route)
  (:split_attribute1
   (&optional __split_attribute1)
   (if __split_attribute1 (setq _split_attribute1 __split_attribute1)) _split_attribute1)
  (:split1
   (&optional __split1)
   (if __split1 (setq _split1 __split1)) _split1)
  (:split_attribute2
   (&optional __split_attribute2)
   (if __split_attribute2 (setq _split_attribute2 __split_attribute2)) _split_attribute2)
  (:split2
   (&optional __split2)
   (if __split2 (setq _split2 __split2)) _split2)
  (:split_attribute3
   (&optional __split_attribute3)
   (if __split_attribute3 (setq _split_attribute3 __split_attribute3)) _split_attribute3)
  (:split3
   (&optional __split3)
   (if __split3 (setq _split3 __split3)) _split3)
  (:attribute2
   (&optional __attribute2)
   (if __attribute2 (setq _attribute2 __attribute2)) _attribute2)
  (:value2
   (&optional __value2)
   (if __value2 (setq _value2 __value2)) _value2)
  (:attribute3
   (&optional __attribute3)
   (if __attribute3 (setq _attribute3 __attribute3)) _attribute3)
  (:value3
   (&optional __value3)
   (if __value3 (setq _value3 __value3)) _value3)
  (:last_event
   (&optional (__last_event :null))
   (if (not (eq __last_event :null)) (setq _last_event __last_event)) _last_event)
  (:first_event
   (&optional (__first_event :null))
   (if (not (eq __first_event :null)) (setq _first_event __first_event)) _first_event)
  (:serialization-length
   ()
   (+
    ;; string _generator_id
    4 (length _generator_id)
    ;; int32 _ID
    4
    ;; string _type
    4 (length _type)
    ;; time _generation_date
    8
    ;; string _gen_time
    4 (length _gen_time)
    ;; time _completed_date
    8
    ;; string _compl_time
    4 (length _compl_time)
    ;; string[] _route
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _route)) 4
    ;; string _split_attribute1
    4 (length _split_attribute1)
    ;; float32 _split1
    4
    ;; string _split_attribute2
    4 (length _split_attribute2)
    ;; float32 _split2
    4
    ;; string _split_attribute3
    4 (length _split_attribute3)
    ;; float32 _split3
    4
    ;; string _attribute2
    4 (length _attribute2)
    ;; float32 _value2
    4
    ;; string _attribute3
    4 (length _attribute3)
    ;; float32 _value3
    4
    ;; bool _last_event
    1
    ;; bool _first_event
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _generator_id
       (write-long (length _generator_id) s) (princ _generator_id s)
     ;; int32 _ID
       (write-long _ID s)
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; time _generation_date
       (write-long (send _generation_date :sec) s) (write-long (send _generation_date :nsec) s)
     ;; string _gen_time
       (write-long (length _gen_time) s) (princ _gen_time s)
     ;; time _completed_date
       (write-long (send _completed_date :sec) s) (write-long (send _completed_date :nsec) s)
     ;; string _compl_time
       (write-long (length _compl_time) s) (princ _compl_time s)
     ;; string[] _route
     (write-long (length _route) s)
     (dolist (elem _route)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string _split_attribute1
       (write-long (length _split_attribute1) s) (princ _split_attribute1 s)
     ;; float32 _split1
       (sys::poke _split1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _split_attribute2
       (write-long (length _split_attribute2) s) (princ _split_attribute2 s)
     ;; float32 _split2
       (sys::poke _split2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _split_attribute3
       (write-long (length _split_attribute3) s) (princ _split_attribute3 s)
     ;; float32 _split3
       (sys::poke _split3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _attribute2
       (write-long (length _attribute2) s) (princ _attribute2 s)
     ;; float32 _value2
       (sys::poke _value2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _attribute3
       (write-long (length _attribute3) s) (princ _attribute3 s)
     ;; float32 _value3
       (sys::poke _value3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _last_event
       (if _last_event (write-byte -1 s) (write-byte 0 s))
     ;; bool _first_event
       (if _first_event (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _generator_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _generator_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _ID
     (setq _ID (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; time _generation_date
     (send _generation_date :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _generation_date :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _gen_time
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _gen_time (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; time _completed_date
     (send _completed_date :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _completed_date :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _compl_time
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _compl_time (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _route
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _route (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _route i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string _split_attribute1
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _split_attribute1 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _split1
     (setq _split1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _split_attribute2
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _split_attribute2 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _split2
     (setq _split2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _split_attribute3
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _split_attribute3 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _split3
     (setq _split3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _attribute2
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _attribute2 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _value2
     (setq _value2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _attribute3
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _attribute3 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _value3
     (setq _value3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _last_event
     (setq _last_event (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _first_event
     (setq _first_event (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get simulator::event :md5sum-) "5783b9c2f01c2af0c22209cf660c120e")
(setf (get simulator::event :datatype-) "simulator/event")
(setf (get simulator::event :definition-)
      "string generator_id
int32 ID
string type
time generation_date
string gen_time
time completed_date
string compl_time
string[] route
string split_attribute1
float32 split1
string split_attribute2
float32 split2
string split_attribute3
float32 split3

string attribute2
float32 value2
string attribute3
float32 value3


bool last_event
bool first_event

")



(provide :simulator/event "5783b9c2f01c2af0c22209cf660c120e")


