// Verileri akıllı kontrat içerisinde kaydedemediğim için buradaki kodlar sadece gelecekte kullanılmak için temel teşkil ediyor.
// Asıl yaptığım proje şu anlık main.rs ve society_analyzer.py içerisinde bulunuyor.

use candid::{CandidType, Deserialize};
use serde::Serialize;

pub static mut CITIZENS: Vec<Citizen> = Vec::new();

#[derive(CandidType, Serialize, Deserialize, Debug)]
pub struct Citizen {
    pub tc: i32,
    pub name: String,
    pub surname: String,
    pub age: i32,
    pub about: String,
}

#[ic_cdk::update]
fn add_citizen(tc: usize, name: String, surname: String, age: usize, about: String) {
    unsafe {
        CITIZENS.push(Citizen {
            tc: tc.try_into().unwrap(),
            name,
            surname,
            age: age.try_into().unwrap(),
            about,
        });
    }
}

#[ic_cdk::query]
fn get_citizens(id: usize) -> String {
    unsafe { format!("{:?}", CITIZENS[id as usize]) }
}
