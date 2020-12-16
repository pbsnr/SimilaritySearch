def build_app(){
  sh 'docker-compose up'
}

def test_app(){
  sh 'sleep 60s'
  sh 'python test_app.py'
}

def stress_test_app(){
  //sh 'docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py'
  echo 'Running stress test'
}

def down_app(){
  //sh 'docker-compose down'
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this
