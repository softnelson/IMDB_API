pipeline {
   agent any  
   stages{

        stage('create container'){
            
            steps{
                sh 'docker-compose up'
               }
           }
        stage('test container') {
            steps {
                    script{    
                        ip = sh(returnStdout: true, script: "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' IMDB_API/www").trim()
                        sh "echo ${ip}"
                        sh "echo ${link}"
                        sh "echo ${porta}"
                    result = sh(returnStdout: true, script: "echo $link$ip$porta").trim()
                    
                    sh "echo '${result}'"
                    container = sh(returnStdout: true, script:"curl -o -I -L -s -w \"%{http_code}\n\" ${result}").trim()
                    
                    sh "echo '${container}'" 
                }
        }        
            
       }
       
   }   
}
