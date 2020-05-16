//Load the file into an NSData object called JSONData

NSError *error = nil;

NSData *JSONData = [NSData dataWithContentsOfFile:filePath options:NSDataReadingMappedIfSafe error:&error];

// Create an Objective-C object from JSON Data

id JSONObject = [NSJSONSerialization
    JSONObjectWithData:JSONData
               options:NSJSONReadingAllowFragments
                 error:&error];
// NSLog(@"%@", JSONObject);
NSMutableDictionary *dict = [[NSMutableDictionary alloc] init];
NSMutableArray *newReport = [[NSMutableArray alloc] init];
NSDictionary *report = JSONObject[@"report"];
for (id myArrayElement in report)
{
    NSDictionary *subject = myArrayElement[@"subject"];
    for (id mySubjectElement in subject)
    {
        dict[@"code"] = mySubjectElement[@"code"];
        dict[@"grade"] = mySubjectElement[@"grade"];
        dict[@"enrollment"] = myArrayElement[@"enrollment"];
        dict[@"name"] = myArrayElement[@"name"];
        [newReport addObject:dict];
        // dict = [String: String]();
    }
};
// NSLog(@"%@", newReport);
NSSortDescriptor *sd = [[NSSortDescriptor alloc] initWithKey:@"code" ascending:YES];
[newReport sortedArrayUsingDescriptors:@[ sd ]];
for (id report in newReport)
{
    NSEnumerator *enu = [report keyEnumerator];
    for (NSString *key in enu)
    {
        // NSLog(@"key : %@",key);
        NSLog(@"%@", [[report valueForKey:key] string]);
    }
};