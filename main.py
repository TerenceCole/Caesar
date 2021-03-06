#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt

#answer = encrypt("Hello, Zach!", 2)
#print(answer)
# => prints Jgnnq, Bcej!

form="""
<form method="post">
    <div>
        <label for="rot">Rotate Your Text by:</label>
        <input type="text" name="rot" value="0">
        <p class="error"></p>
    </div>
    <textarea type="text" name="answer">%(answer)s</textarea>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):

    def write_form(self, answer=""):
        self.response.write(form % {"answer": answer})

    def get(self):
        self.write_form()

    def post(self):
        userAnswer = self.request.get("answer")
        userRot = int(self.request.get("rot"))
        encryptedAnswer = encrypt(userAnswer, userRot)
        self.write_form(encryptedAnswer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
