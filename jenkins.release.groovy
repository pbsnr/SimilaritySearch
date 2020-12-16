def build_app(){
  sh 'docker-compose up -d'
}


def user_acceptance(){
  input "proceed with deployment to live ?"
}

def test_app(){
  sh 'python test_app.py'
}

def stress_test_app(){
}

def down_app(){
  sh 'docker-compose down'
}

def release_app(){
}

def live_app(){
  user_acceptance()
  echo 'merge with main'
}

return this
